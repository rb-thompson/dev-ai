import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

def calculate_relativistic_effects(altitude, velocity, ground_radius=6371e3, period=86400):
    """
    Calculate combined general and special relativistic effects for an ISS clock vs. ground clock.

    Args:
        altitude (float): Altitude of ISS above Earth's surface in meters (e.g., 400e3).
        velocity (float): Orbital velocity in m/s (e.g., 7800 for ISS).
        ground_radius (float): Earth's radius in meters (default: 6371 km).
        period (float): Time period in seconds (default: 1 day).

    Returns:
        dict: General, special, and total fractional shifts, time differences, and frequency shifts.
    """
    # Constants
    G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
    M = 5.972e24     # Earth's mass (kg)
    c = 2.99792458e8 # Speed of light (m/s)
    cesium_freq = 9_192_631_770  # Cesium clock frequency (Hz)

    # Distances from Earth's center
    r_ground = ground_radius
    r_iss = ground_radius + altitude

    # General Relativity: Gravitational redshift
    phi_ground = -G * M / r_ground
    phi_iss = -G * M / r_iss
    delta_phi = phi_iss - phi_ground
    frac_shift_gr = delta_phi / (c ** 2)

    # Special Relativity: Velocity time dilation
    frac_shift_sr = -(velocity ** 2) / (2 * c ** 2)

    # Total fractional frequency shift
    frac_shift_total = frac_shift_gr + frac_shift_sr

    # Time differences
    time_diff_gr = period * frac_shift_gr
    time_diff_sr = period * frac_shift_sr
    time_diff_total = period * frac_shift_total

    # Frequency shifts
    freq_shift_gr = cesium_freq * frac_shift_gr
    freq_shift_sr = cesium_freq * frac_shift_sr
    freq_shift_total = cesium_freq * frac_shift_total

    return {
        "General Relativity": {
            "Fractional Shift": frac_shift_gr,
            "Time Difference (s)": time_diff_gr,
            "Time Difference (ns)": time_diff_gr * 1e9,
            "Frequency Shift (Hz)": freq_shift_gr
        },
        "Special Relativity": {
            "Fractional Shift": frac_shift_sr,
            "Time Difference (s)": time_diff_sr,
            "Time Difference (ns)": time_diff_sr * 1e9,
            "Frequency Shift (Hz)": freq_shift_sr
        },
        "Total": {
            "Fractional Shift": frac_shift_total,
            "Time Difference (s)": time_diff_total,
            "Time Difference (ns)": time_diff_total * 1e9,
            "Frequency Shift (Hz)": freq_shift_total
        }
    }

def simulate_aces_mission(setups, period=86400):
    """
    Simulate ACES mission for multiple setups.

    Args:
        setups (list): List of tuples (setup_name, altitude in meters, velocity in m/s).
        period (float): Observation period in seconds.

    Returns:
        dict: Results for each setup.
    """
    results = {}
    for name, altitude, velocity in setups:
        data = calculate_relativistic_effects(altitude, velocity, period=period)
        results[name] = {
            "Altitude (km)": altitude / 1000,
            "Velocity (km/s)": velocity / 1000,
            **data
        }
    return results

# Set up simulation parameters
setups = [
    ("ISS ACES Mission", 400e3, 7800),  # ISS: 400 km, ~7.8 km/s
    ("Ground Reference", 0, 0),         # Ground: 0 km, 0 m/s
]
periods = {
    "One Day": 86400,
    "25 Days": 25 * 86400
}

# Initialize Dash app with a dark theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Dashboard layout
app.layout = dbc.Container([
    html.H1("ACES Mission: Relativistic Clock Simulation", style={
        "color": "#00FFFF", "textAlign": "center", "fontFamily": "Roboto",
        "marginTop": 20, "marginBottom": 20
    }),
    html.Hr(style={"borderColor": "#00FF00"}),
    
    # Dropdown for period selection
    dbc.Row([
        dbc.Col([
            html.Label("Select Observation Period:", style={"color": "#FFFFFF"}),
            dcc.Dropdown(
                id="period-dropdown",
                options=[{"label": name, "value": value} for name, value in periods.items()],
                value=86400,
                style={"backgroundColor": "#1E1E1E", "color": "#000000"}
            )
        ], width=4)
    ], style={"marginBottom": 20}),
    
    # Results table
    html.H3("Simulation Results", style={"color": "#00FF00", "fontFamily": "Roboto"}),
    html.Div(id="results-table", style={"marginBottom": 20}),
    
    # Bar chart for relativistic effects
    html.H3("Relativistic Effects Comparison", style={"color": "#00FF00", "fontFamily": "Roboto"}),
    dcc.Graph(id="bar-chart", style={"backgroundColor": "#1E1E1E"}),
    
    # Line plot for time difference accumulation
    html.H3("Time Difference Accumulation", style={"color": "#00FF00", "fontFamily": "Roboto"}),
    dcc.Graph(id="line-plot", style={"backgroundColor": "#1E1E1E"})
], fluid=True, style={"backgroundColor": "#121212", "padding": 20})

# Callback to update table and plots
@app.callback(
    [Output("results-table", "children"),
     Output("bar-chart", "figure"),
     Output("line-plot", "figure")],
    [Input("period-dropdown", "value")]
)
def update_dashboard(period):
    # Run simulation
    results = simulate_aces_mission(setups, period=period)
    
    # Build table
    table_data = []
    for name, data in results.items():
        for effect in ["General Relativity", "Special Relativity", "Total"]:
            table_data.append({
                "Setup": name,
                "Effect": effect,
                "Altitude (km)": f"{data['Altitude (km)']:.0f}",
                "Velocity (km/s)": f"{data['Velocity (km/s)']:.2f}",
                "Frac. Shift": f"{data[effect]['Fractional Shift']:.2e}",
                "Time Diff (ns)": f"{data[effect]['Time Difference (ns)']:.2f}",
                "Freq. Shift (Hz)": f"{data[effect]['Frequency Shift (Hz)']:.4f}"
            })
    df_table = pd.DataFrame(table_data)
    table = dbc.Table.from_dataframe(
        df_table,
        striped=True,
        bordered=True,
        hover=True,
        style={
            "backgroundColor": "#1E1E1E",
            "color": "#FFFFFF",
            "borderColor": "#00FF00",
            "fontFamily": "Roboto"
        }
    )
    
    # Bar chart: Compare relativistic effects
    bar_data = []
    for name, data in results.items():
        if name == "ISS ACES Mission":  # Only show ISS for clarity
            for effect in ["General Relativity", "Special Relativity", "Total"]:
                bar_data.append({
                    "Effect": effect,
                    "Fractional Shift": data[effect]["Fractional Shift"]
                })
    df_bar = pd.DataFrame(bar_data)
    bar_fig = px.bar(
        df_bar,
        x="Effect",
        y="Fractional Shift",
        title="Fractional Frequency Shift by Effect",
        color="Effect",
        color_discrete_map={
            "General Relativity": "#00FFFF",
            "Special Relativity": "#FF00FF",
            "Total": "#00FF00"
        }
    )
    bar_fig.update_layout(
        plot_bgcolor="#1E1E1E",
        paper_bgcolor="#1E1E1E",
        font={"color": "#FFFFFF", "family": "Roboto"},
        title={"x": 0.5, "font": {"color": "#00FFFF"}},
        xaxis={"gridcolor": "#444444"},
        yaxis={"gridcolor": "#444444"}
    )
    
    # Line plot: Time difference accumulation
    time_points = [period * i / 100 for i in range(101)]  # 100 points up to period
    line_data = []
    for t in time_points:
        iss_data = calculate_relativistic_effects(400e3, 7800, period=t)
        line_data.append({
            "Time (days)": t / 86400,
            "Time Difference (ns)": iss_data["Total"]["Time Difference (ns)"]
        })
    df_line = pd.DataFrame(line_data)
    line_fig = px.line(
        df_line,
        x="Time (days)",
        y="Time Difference (ns)",
        title="Time Difference Accumulation (ISS vs. Ground)",
        color_discrete_sequence=["#00FFFF"]
    )
    line_fig.update_layout(
        plot_bgcolor="#1E1E1E",
        paper_bgcolor="#1E1E1E",
        font={"color": "#FFFFFF", "family": "Roboto"},
        title={"x": 0.5, "font": {"color": "#00FFFF"}},
        xaxis={"gridcolor": "#444444"},
        yaxis={"gridcolor": "#444444"}
    )
    
    return table, bar_fig, line_fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)