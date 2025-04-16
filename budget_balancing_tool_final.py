import streamlit as st
import pandas as pd

# --- Forecasting logic ---
def forecast_non_decreasing(df, partner, total_budget_dict, yearly_growth=0.03):
    hist = df[df["Partner"] == partner].pivot(index="Year", columns="Category", values="Amount").fillna(0)
    recent = hist.loc[2025]
    known_growth_cats = {
        "Total Community Engagement Costs": 0.04,
        "Total Monitoring and Evaluation Costs": 0.03,
        "Total Human Resources": 0.025,
    }
    rows = []
    for year, total in total_budget_dict.items():
        for cat in recent.index:
            base = recent[cat]
            growth = known_growth_cats.get(cat, yearly_growth)
            years_ahead = year - 2025
            estimate = round(base * ((1 + growth) ** years_ahead), 2)
            rows.append([partner, year, cat, estimate])
    return pd.DataFrame(rows, columns=["Partner", "Year", "Category", "Amount"])

# --- Sample static projections (final version loads real forecasts) ---
partner_data = {   'ASDF': {   2026: {   'Capital Investments': 0.0,
                          'Community Engagement': 51490.8,
                          'Human Resources': 181348.85,
                          'Hygiene & Sanitation': 11292.57,
                          'Monitoring & Evaluation': 30223.2,
                          'Office Costs': 14001.2,
                          'Operations & Maintenance': 12062.08,
                          'Water Program Costs': 291254.12},
                2027: {   'Capital Investments': 0.0,
                          'Community Engagement': 51509.98,
                          'Human Resources': 188613.57,
                          'Hygiene & Sanitation': 11134.48,
                          'Monitoring & Evaluation': 32644.09,
                          'Office Costs': 13217.1,
                          'Operations & Maintenance': 9423.98,
                          'Water Program Costs': 302879.83},
                2028: {   'Capital Investments': 0.0,
                          'Community Engagement': 52405.72,
                          'Human Resources': 199506.37,
                          'Hygiene & Sanitation': 11165.36,
                          'Monitoring & Evaluation': 35858.69,
                          'Office Costs': 12689.16,
                          'Operations & Maintenance': 10171.77,
                          'Water Program Costs': 305908.63},
                2029: {   'Capital Investments': 0.0,
                          'Community Engagement': 53252.66,
                          'Human Resources': 210773.41,
                          'Hygiene & Sanitation': 11182.81,
                          'Monitoring & Evaluation': 39342.27,
                          'Office Costs': 12167.61,
                          'Operations & Maintenance': 10850.43,
                          'Water Program Costs': 308967.71},
                2030: {   'Capital Investments': 0.0,
                          'Community Engagement': 53879.36,
                          'Human Resources': 221714.11,
                          'Hygiene & Sanitation': 11151.85,
                          'Monitoring & Evaluation': 42977.69,
                          'Office Costs': 11617.04,
                          'Operations & Maintenance': 10735.62,
                          'Water Program Costs': 313857.32}},
    'FOTF': {   2026: {   'Total Capital Investments': 0.0,
                          'Total Community Engagement Costs': 15084.3,
                          'Total Human Resources': 88471.29,
                          'Total Hygiene and Sanitation Costs': 4345.85,
                          'Total Monitoring and Evaluation Costs': 3336.86,
                          'Total Office Costs': 10606.45,
                          'Total Operations and Maintenance Costs': 6502.19,
                          'Total Other': 0.0,
                          'Total Project Budget': 160931.42,
                          'Total Water Program Costs': 32297.96},
                2027: {   'Total Capital Investments': 0.0,
                          'Total Community Engagement Costs': 15687.67,
                          'Total Human Resources': 90683.07,
                          'Total Hygiene and Sanitation Costs': 4476.22,
                          'Total Monitoring and Evaluation Costs': 3436.97,
                          'Total Office Costs': 10924.64,
                          'Total Operations and Maintenance Costs': 6697.26,
                          'Total Other': 0.0,
                          'Total Project Budget': 165759.37,
                          'Total Water Program Costs': 33266.9},
                2028: {   'Total Capital Investments': 0.0,
                          'Total Community Engagement Costs': 16315.17,
                          'Total Human Resources': 92950.15,
                          'Total Hygiene and Sanitation Costs': 4610.51,
                          'Total Monitoring and Evaluation Costs': 3540.07,
                          'Total Office Costs': 11252.38,
                          'Total Operations and Maintenance Costs': 6898.18,
                          'Total Other': 0.0,
                          'Total Project Budget': 170732.15,
                          'Total Water Program Costs': 34264.9},
                2029: {   'Total Capital Investments': 0.0,
                          'Total Community Engagement Costs': 16967.78,
                          'Total Human Resources': 95273.9,
                          'Total Hygiene and Sanitation Costs': 4748.83,
                          'Total Monitoring and Evaluation Costs': 3646.28,
                          'Total Office Costs': 11589.95,
                          'Total Operations and Maintenance Costs': 7105.12,
                          'Total Other': 0.0,
                          'Total Project Budget': 175854.11,
                          'Total Water Program Costs': 35292.85},
                2030: {   'Total Capital Investments': 0.0,
                          'Total Community Engagement Costs': 17646.49,
                          'Total Human Resources': 97655.75,
                          'Total Hygiene and Sanitation Costs': 4891.29,
                          'Total Monitoring and Evaluation Costs': 3755.67,
                          'Total Office Costs': 11937.65,
                          'Total Operations and Maintenance Costs': 7318.28,
                          'Total Other': 0.0,
                          'Total Project Budget': 181129.73,
                          'Total Water Program Costs': 36351.64}},
    "Mariatu's Hope": {   2026: {   'Total Capital Investments': 0.0,
                                    'Total Community Engagement Costs': 11005.91,
                                    'Total Human Resources': 182762.15,
                                    'Total Hygiene and Sanitation Costs': 2294.66,
                                    'Total Monitoring and Evaluation Costs': 12352.14,
                                    'Total Office Costs': 59729.7,
                                    'Total Operations and Maintenance Costs': 5174.18,
                                    'Total Other': 0.0,
                                    'Total Project Budget': 448128.32,
                                    'Total Water Program Costs': 174023.88},
                          2027: {   'Total Capital Investments': 0.0,
                                    'Total Community Engagement Costs': 11446.15,
                                    'Total Human Resources': 187331.21,
                                    'Total Hygiene and Sanitation Costs': 2363.5,
                                    'Total Monitoring and Evaluation Costs': 12722.71,
                                    'Total Office Costs': 61521.59,
                                    'Total Operations and Maintenance Costs': 5329.41,
                                    'Total Other': 0.0,
                                    'Total Project Budget': 461572.17,
                                    'Total Water Program Costs': 179244.59},
                          2028: {   'Total Capital Investments': 0.0,
                                    'Total Community Engagement Costs': 11904.0,
                                    'Total Human Resources': 192014.49,
                                    'Total Hygiene and Sanitation Costs': 2434.41,
                                    'Total Monitoring and Evaluation Costs': 13104.39,
                                    'Total Office Costs': 63367.24,
                                    'Total Operations and Maintenance Costs': 5489.29,
                                    'Total Other': 0.0,
                                    'Total Project Budget': 475419.34,
                                    'Total Water Program Costs': 184621.93},
                          2029: {   'Total Capital Investments': 0.0,
                                    'Total Community Engagement Costs': 12380.16,
                                    'Total Human Resources': 196814.85,
                                    'Total Hygiene and Sanitation Costs': 2507.44,
                                    'Total Monitoring and Evaluation Costs': 13497.52,
                                    'Total Office Costs': 65268.26,
                                    'Total Operations and Maintenance Costs': 5653.97,
                                    'Total Other': 0.0,
                                    'Total Project Budget': 489681.92,
                                    'Total Water Program Costs': 190160.59},
                          2030: {   'Total Capital Investments': 0.0,
                                    'Total Community Engagement Costs': 12875.36,
                                    'Total Human Resources': 201735.22,
                                    'Total Hygiene and Sanitation Costs': 2582.67,
                                    'Total Monitoring and Evaluation Costs': 13902.44,
                                    'Total Office Costs': 67226.3,
                                    'Total Operations and Maintenance Costs': 5823.59,
                                    'Total Other': 0.0,
                                    'Total Project Budget': 504372.37,
                                    'Total Water Program Costs': 195865.41}},
    'TWT': {   2026: {   'Total Capital Investments': 0.0,
                         'Total Community Engagement Costs': 6645.66,
                         'Total Human Resources': 77815.88,
                         'Total Hygiene and Sanitation Costs': 17354.58,
                         'Total Monitoring and Evaluation Costs': 8047.65,
                         'Total Office Costs': 12934.48,
                         'Total Operations and Maintenance Costs': 7079.75,
                         'Total Other': 0.0,
                         'Total Project Budget': 207665.95,
                         'Total Water Program Costs': 77472.25},
               2027: {   'Total Capital Investments': 0.0,
                         'Total Community Engagement Costs': 6911.49,
                         'Total Human Resources': 79761.28,
                         'Total Hygiene and Sanitation Costs': 17875.22,
                         'Total Monitoring and Evaluation Costs': 8289.08,
                         'Total Office Costs': 13322.52,
                         'Total Operations and Maintenance Costs': 7292.14,
                         'Total Other': 0.0,
                         'Total Project Budget': 213895.93,
                         'Total Water Program Costs': 79796.42},
               2028: {   'Total Capital Investments': 0.0,
                         'Total Community Engagement Costs': 7187.95,
                         'Total Human Resources': 81755.31,
                         'Total Hygiene and Sanitation Costs': 18411.48,
                         'Total Monitoring and Evaluation Costs': 8537.75,
                         'Total Office Costs': 13722.19,
                         'Total Operations and Maintenance Costs': 7510.9,
                         'Total Other': 0.0,
                         'Total Project Budget': 220312.81,
                         'Total Water Program Costs': 82190.31},
               2029: {   'Total Capital Investments': 0.0,
                         'Total Community Engagement Costs': 7475.47,
                         'Total Human Resources': 83799.19,
                         'Total Hygiene and Sanitation Costs': 18963.82,
                         'Total Monitoring and Evaluation Costs': 8793.88,
                         'Total Office Costs': 14133.86,
                         'Total Operations and Maintenance Costs': 7736.23,
                         'Total Other': 0.0,
                         'Total Project Budget': 226922.19,
                         'Total Water Program Costs': 84656.02},
               2030: {   'Total Capital Investments': 0.0,
                         'Total Community Engagement Costs': 7774.49,
                         'Total Human Resources': 85894.17,
                         'Total Hygiene and Sanitation Costs': 19532.74,
                         'Total Monitoring and Evaluation Costs': 9057.7,
                         'Total Office Costs': 14557.87,
                         'Total Operations and Maintenance Costs': 7968.32,
                         'Total Other': 0.0,
                         'Total Project Budget': 233729.86,
                         'Total Water Program Costs': 87195.7}},
    'WEWASAFO': {   2026: {   'Total Capital Investments': 0.0,
                              'Total Community Engagement Costs': 19424.88,
                              'Total Human Resources': 277193.08,
                              'Total Hygiene and Sanitation Costs': 652846.87,
                              'Total Monitoring and Evaluation Costs': 27172.0,
                              'Total Office Costs': 10497.49,
                              'Total Operations and Maintenance Costs': 2792.92,
                              'Total Other': 0.0,
                              'Total Project Budget': 795026.66,
                              'Total Water Program Costs': 381477.65},
                    2027: {   'Total Capital Investments': 0.0,
                              'Total Community Engagement Costs': 20201.88,
                              'Total Human Resources': 284122.9,
                              'Total Hygiene and Sanitation Costs': 672432.27,
                              'Total Monitoring and Evaluation Costs': 27987.16,
                              'Total Office Costs': 10812.42,
                              'Total Operations and Maintenance Costs': 2876.7,
                              'Total Other': 0.0,
                              'Total Project Budget': 818877.46,
                              'Total Water Program Costs': 392921.98},
                    2028: {   'Total Capital Investments': 0.0,
                              'Total Community Engagement Costs': 21009.95,
                              'Total Human Resources': 291225.98,
                              'Total Hygiene and Sanitation Costs': 692605.24,
                              'Total Monitoring and Evaluation Costs': 28826.77,
                              'Total Office Costs': 11136.79,
                              'Total Operations and Maintenance Costs': 2963.01,
                              'Total Other': 0.0,
                              'Total Project Budget': 843443.78,
                              'Total Water Program Costs': 404709.64},
                    2029: {   'Total Capital Investments': 0.0,
                              'Total Community Engagement Costs': 21850.35,
                              'Total Human Resources': 298506.63,
                              'Total Hygiene and Sanitation Costs': 713383.4,
                              'Total Monitoring and Evaluation Costs': 29691.58,
                              'Total Office Costs': 11470.89,
                              'Total Operations and Maintenance Costs': 3051.9,
                              'Total Other': 0.0,
                              'Total Project Budget': 868747.09,
                              'Total Water Program Costs': 416850.93},
                    2030: {   'Total Capital Investments': 0.0,
                              'Total Community Engagement Costs': 22724.36,
                              'Total Human Resources': 305969.29,
                              'Total Hygiene and Sanitation Costs': 734784.9,
                              'Total Monitoring and Evaluation Costs': 30582.32,
                              'Total Office Costs': 11815.02,
                              'Total Operations and Maintenance Costs': 3143.45,
                              'Total Other': 0.0,
                              'Total Project Budget': 894809.51,
                              'Total Water Program Costs': 429356.46}}}  # Loaded dynamically from memory after projections

# --- UI Setup ---
st.set_page_config(page_title="Budget Balancer", layout="wide")
st.markdown("""
    <style>
        .stNumberInput > div > div > input {
            font-size: 20px !important;
            font-weight: 600;
            color: #333333;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            font-size: 26px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Multi-Partner Budget Balancing Tool")

# Partner and year selection
partner_names = list(partner_data.keys())
selected_partner = st.selectbox("Select Partner Organization", partner_names)

if selected_partner:
    years = sorted(partner_data[selected_partner].keys())
    selected_year = st.selectbox("Select Year", years, key=f"year_selector_{selected_partner}")
    base_allocation = partner_data[selected_partner][selected_year]
    initial_total_budget = base_allocation.get("Total Project Budget", sum(base_allocation.values()))
else:
    st.warning("No partner data available.")
    st.stop()

# Editable total budget
total_budget = st.number_input("Total Budget for Year ($)", value=round(initial_total_budget, 2), min_value=0.0)

# Default project types per partner
partner_projects = {
    "ASDF": {
        "Sand Dam": 13542.71,
        "Shallow Well": 1810.72,
        "RWHT": 6828.91,
        "Solar": 30723.82
    },
    "Mariatu's Hope": {
        "Borehole": 6025.00,
        "Conversion": 3771.86
    },
    "TWT": {
        "Borehole": 7521.58
    },
    "WEWASAFO": {
        "Borehole": 8301.63,
        "Spring": 859.23
    },
    "FOTF": {
        "Borehole": 6912.00,
        "Spring": 856.17
    }
}

# Water Program Inputs
st.subheader("Set Water Program by Project Counts")
project_types = partner_projects.get(selected_partner, {})
col_a, col_b = st.columns(2)
project_counts = {}
project_costs = {}

with col_a:
    for project in project_types:
        project_counts[project] = st.number_input(f"{project} (Qty)", min_value=0, value=0)

with col_b:
    for project, default_cost in project_types.items():
        project_costs[project] = st.number_input(f"Cost per {project}", value=default_cost)

water_program_total = sum(project_counts[p] * project_costs[p] for p in project_types)
st.markdown(f"**Calculated Water Program Total:** ${water_program_total:,.2f}")

base_allocation["Water Program Costs"] = round(water_program_total, 2)

# Adjust and lock controls
manual_adjustments = {"Water Program Costs": round(water_program_total, 2)}
locked_cats = st.multiselect("Lock categories from adjustment", options=base_allocation.keys(), key=f"locks_{selected_year}")

# Inputs and allocation view
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Adjust by Amount ($)")
    for category in base_allocation:
        if category != "Water Program Costs":
            input_val = st.number_input(
                f"{category} ($)",
                min_value=0.0,
                value=float(base_allocation[category]),
                key=f"input_{selected_year}_{category}_amount"
            )
            if input_val != float(base_allocation[category]):
                manual_adjustments[category] = input_val

def balance_budget_adjustment(total_budget, manual_adjustments, base_allocation, locked=[]):
    import copy
    new_allocation = copy.deepcopy(base_allocation)
    for category, new_value in manual_adjustments.items():
        new_allocation[category] = new_value
    allocated = sum(new_allocation[c] for c in manual_adjustments)
    remaining_budget = total_budget - allocated
    adjustable_cats = [c for c in base_allocation.keys() if c not in manual_adjustments and c not in locked]
    total_adjustable = sum(base_allocation[c] for c in adjustable_cats)
    if total_adjustable == 0:
        for cat in adjustable_cats:
            new_allocation[cat] = 0
        return new_allocation
    for cat in adjustable_cats:
        share = base_allocation[cat] / total_adjustable
        new_allocation[cat] = round(remaining_budget * share, 2)
    return new_allocation

# Rebalance and render outputs
updated_allocation = balance_budget_adjustment(
    total_budget,
    manual_adjustments,
    base_allocation,
    locked=list(locked_cats)
)

with col2:
    st.markdown("#### Updated Allocation")
    for category in [c for c in base_allocation if c != "Water Program Costs"]:
        st.number_input(
            f"{category} (Adjusted)",
            value=round(updated_allocation[category], 2),
            disabled=True,
            key=f"updated_{selected_year}_{category}"
        )
    st.number_input(
        "Water Program Costs (Adjusted)",
        value=round(updated_allocation["Water Program Costs"], 2),
        disabled=True,
        key=f"updated_{selected_year}_Water_Program_Costs"
    )
