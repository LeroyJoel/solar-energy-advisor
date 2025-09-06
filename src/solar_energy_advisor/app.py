import streamlit as st
from dotenv import load_dotenv
from solar_energy_advisor.crew import SolarEnergyAdvisor
import os

def generate_report(user_input):
    """
    Generates the solar energy report using the SolarEnergyAdvisor crew.
    """
    inputs = {"user_input": user_input}
    crew = SolarEnergyAdvisor().crew()
    result = crew.kickoff(inputs=inputs)
    return result

def main():
    """
    Main function to run the Streamlit app.
    """
    load_dotenv()
    st.set_page_config(page_title="Solar Energy Advisor", page_icon="☀️", layout="wide")

    st.title("☀️ Solar Energy Advisor")
    st.markdown(
        """
        <p style='font-size: 20px;'>
            Welcome to the Solar Energy Advisor! This tool helps you determine the best solar energy solution for your home or business in Nigeria.
            Simply enter your location, the appliances you need to power, and your budget, and we'll generate a detailed report for you.
        </p>
        """,
        unsafe_allow_html=True,
    )

    user_input = st.text_input(
        "Enter your requirements:",
        "I live in Abuja and need to power 4 fans, 1 fridge, and 6 bulbs. Budget ₦1,000,000.",
    )

    if st.button("Generate Report"):
        with st.spinner("Generating your report..."):
            report = generate_report(user_input)
            st.success("Report generated successfully!")

            st.markdown("---")
            st.header("Generated Report")
            st.markdown(report, unsafe_allow_html=True)

            st.markdown("---")
            st.download_button(
                label="Download Report",
                data=str(report),
                file_name="solar_energy_report.md",
                mime="text/markdown",
            )

if __name__ == "__main__":
    main()
