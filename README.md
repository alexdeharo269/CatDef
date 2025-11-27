# AED and OHCA Analysis Project

## Description

This project explores the relationship between Automated External Defibrillator (AED) and multiple different variables. The distance to and from AEDs, the socio-demographic (from poverty to age) variables, the Out-of-Hospital Cardiac Arrests (OHCA) incidence and type of locations and accessability to the AEDs will be studied. The analysis is organized into subfolders representing different collaborators’ contributions, each focusing on specific aspects of AED coverage and cardiac arrest data.

The repository includes processed data, geospatial files, scripts, and plots to facilitate reproducibility and further analysis.

---

## Requirements

The project uses Python 3 and dependencies listed in `requirements.txt`.

You can install the requirements via:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
.
├── alejandro/
├── eulalia/
├── jan/
├── javier/
├── german/
|
├── data/
├── carto/
└── README.md
```

### Folder Details

* **alejandro**
  Codes and plots analyzing **AED coverage and distance to the nearest AED**.

* **eulalia**
  Codes and plots analyzing **AED location types**.

* **german**
  Codes and plots analyzing **socio-demographic factors and AED coverage**.

* **jan**
  Codes and plots analyzing the relationship between **AED coverage and OHCA**.

* **javier**
  Codes and plots analyzing **AED coverage and age-related factors**.

* **data**
  Contains CSV files with medical records and other processed datasets.

* **carto**
  GeoJSON files for geospatial mapping and visualization of administrative areas.

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/alexdeharo269/CatDef.git
cd CatDef
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Open the Jupyter notebooks in the corresponding folders to run analyses and generate plots.

---

## License

This repository is released under the **MIT License**.
Data files are also licensed under the **MIT License** unless otherwise stated.

---

## Contact

For questions or further details, please contact the project contributors through GitHub.
