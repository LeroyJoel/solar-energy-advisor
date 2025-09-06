# ☀️ Solar Energy Advisor Crew
## 📌 Project Overview

The Solar Energy Advisor Crew helps Nigerian households and SMEs transition from costly, unreliable grid electricity and fuel generators to affordable solar energy systems.

The system analyzes a user’s energy needs, recommends the right solar inverter system size, estimates the cost in Nigerian Naira (₦), suggests financing options, and compares long-term savings versus generator use.

This solution directly addresses Nigeria’s energy poverty challenge by making solar adoption simple and practical.

## 🚀 Features

1. ⚡ Energy Needs Assessment → Calculates household/business load in kVA & daily kWh.

2. 🔋 Solar System Recommendation → Suggests inverter size, batteries, and panels.

3. 💰 Cost & Financing Advisor → Estimates cost in ₦ and suggests cooperative loans, bank financing, or pay-as-you-go solar.

4. 📊 Solar Advisory Report Generator → Creates a clear report comparing solar vs. generator expenses.

5. 🌍 Nigerian Context → Tailored for Nigerian households & SMEs, with costs in ₦.

6. 🖥️ Streamlit App → Simple, interactive web app where users input their appliances, budget, and location to receive instant recommendations.

## 🧩 CrewAI Agents & Tasks

**Agents:**

- energy_needs_assessor → Calculates appliance load.

- solar_system_recommender → Recommends inverter, panels, and batteries.

- cost_financing_advisor → Estimates cost in ₦ and financing options.

- solar_report_generator → Creates the final report.

**Tasks:**

- assess_energy_needs_task → Appliance & load calculation.

- recommend_solar_system_task → Recommend solar setup.

- calculate_costs_task → Estimate ₦ cost + financing.

- generate_solar_report_task → Produce the advisory report.

## How to Run the Application

1.  **Install the dependencies:**

    ```bash
    pip install -e .
    ```

2.  **Run the Streamlit app:**

    ```bash
    streamlit run src/solar_energy_advisor/app.py
    ```

3.  **Open your web browser and navigate to the provided URL.**

**Users can:**

- Select appliances & number of units

- Input location (e.g., Lagos, Abuja, Ibadan)

- Enter budget (in ₦)

- Get an instant Solar Energy Report
- Downoad the report

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/LeroyJoel/solar-energy-advisor
cd solar-energy-advisor-crew

2. Install Dependencies
pip install -r requirements.txt

3. Run the CrewAI Backend
python main.py

4. Launch the Streamlit App
streamlit run app.py

## 📌 Future Improvements

- Integrate live solar equipment price APIs for real-time costs.

- Add geo-mapping of certified Nigerian solar installers.

- Extend financing integration with banks and pay-as-you-go providers.