import streamlit as st

# Application title
st.title("Welcome to TechFix Computer Repair Services")

# Sidebar
st.sidebar.title("Our Services")
st.sidebar.info("Explore the wide range of services we offer to get your computer up and running.")

# Introduction Section
st.header("Your One-Stop Solution for Computer Repairs")
st.write(
    """
    At TechFix, we offer comprehensive computer repair and maintenance services to keep your systems running smoothly. 
    Whether it's a hardware issue, software problem, or network setup, we've got you covered!
    """
)

# Services Section
st.header("Our Services")

# Categorized Services
st.subheader("🔧 Hardware Repairs and Upgrades")
hardware_services = [
    "Screen Replacement",
    "Keyboard Replacement or Repair",
    "Battery Replacement",
    "Hard Drive Replacement (HDD or SSD upgrades)",
    "RAM (Memory) Upgrade or Replacement",
    "Motherboard Repair or Replacement",
    "Power Supply Replacement (desktops)",
    "Fan Repair or Replacement (cooling issues)",
    "Peripheral Repairs (printers, scanners, etc.)",
    "Graphics Card Repairs or Upgrades",
    "External Drive Repairs"
]
st.write(", ".join(hardware_services))

st.subheader("🖥️ Software Services")
software_services = [
    "Operating System Installation or Reinstallation (Windows, macOS, Linux)",
    "System Optimization (speed enhancement, cleaning junk files)",
    "Software Installation (e.g., Office Suite, Adobe products)",
    "Driver Installation or Updates",
    "Data Recovery and Backup Services",
    "Virus, Malware, and Spyware Removal",
    "Blue Screen and Error Code Fixing",
    "Software Troubleshooting and Bug Fixing",
    "File System Repairs (e.g., corrupted drives)"
]
st.write(", ".join(software_services))

st.subheader("🌐 Networking and Connectivity")
networking_services = [
    "Wi-Fi Setup and Troubleshooting",
    "Ethernet Cable Installation",
    "Network Printer Setup",
    "Internet Connectivity Repairs",
    "Network Security Setup (firewalls, secure access points)",
    "VPN Configuration",
    "Server Installation or Maintenance"
]
st.write(", ".join(networking_services))

st.subheader("🛠️ Diagnostic and Assessment Services")
diagnostic_services = [
    "Hardware Diagnostics",
    "Software Health Checks",
    "Network Analysis and Troubleshooting",
    "Pre-purchase System Consultation",
    "Second Opinions on Repairs"
]
st.write(", ".join(diagnostic_services))

st.subheader("🎮 Custom Services")
custom_services = [
    "Custom PC Building",
    "Gaming System Setup or Repairs",
    "Workstation Optimization",
    "Overclocking Services (for gaming or high-performance systems)"
]
st.write(", ".join(custom_services))

st.subheader("📱 Specialized Services")
specialized_services = [
    "Apple/Mac Repairs",
    "Laptop Repair (hinges, ultrabook components)",
    "Tablet or Hybrid Device Repairs",
    "Liquid Damage Repairs",
    "Data Encryption and Decryption Services",
    "IT Asset Disposal and Recycling",
    "Data Shredding (secure deletion)"
]
st.write(", ".join(specialized_services))

st.subheader("💼 Business-Oriented IT Services")
business_services = [
    "Server Setup and Maintenance",
    "Remote Desktop Configuration",
    "Cloud Integration Services",
    "On-site IT Support",
    "IT Infrastructure Setup"
]
st.write(", ".join(business_services))

# Call to Action
st.header("📞 Contact Us Today!")
st.write(
    """
    Need help with your computer? Reach out to us for fast and reliable services.
    Call us at **(123) 456-7890** or email us at **support@techfix.com**.
    """
)

# Footer
st.write("---")
st.write("© 2024 TechFix Computer Repair Services. All rights reserved.")
