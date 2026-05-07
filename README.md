
# 🩺 Diabetes Prediction - Big Data Analysis

An end-to-end Big Data processing pipeline designed to analyze **100k records** for diabetes prediction. This project is fully containerized using **Docker** to ensure consistency across all environments.

## 🚀 Features
- **Automated Cleaning:** Robust handling of duplicates and missing values (Mode Imputation).
- **Deep Visualization:** Generation of **7 analytical plots** (Distribution, Correlation, Boxplots, etc.).
- **Data Engineering:** Integrated Preprocessing (One-Hot Encoding, Label Encoding, and MinMax Scaling).
- **Production Ready:** Fully Dockerized with optimized image layers.

## 🛠️ Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

## 💻 How to Run (Option 1: Build from Source)

If you have the source code and want to build the environment locally:

1. **Build the image:**
   ```bash
   docker build -t big-data-project .
   ```

2. **Run the container (Volume Mapping):**
   *(This will generate the 7 result images in your current folder)*
   ```bash
   docker run -v "%cd%:/app" big-data-project
   ```
## 📦 Portable Version (Option 2: Pre-built Image)

Use this option if you want to run the project without building it from the Dockerfile.

### 1. Download the Image
- **[Download big-data-project.tar](https://drive.google.com/file/d/1dpp2KcNE3RgTzzXKwzMZLi512HHIDs-e/view?usp=sharing)** - **Size:** 168 MB

### 2. Load and Execution
Open your CMD in the folder where the `.tar` file is located and run:

```bash
# Load the image into Docker
docker load -i big-data-project.tar

# Run the container (Mapping results to your folder)
docker run -v "%cd%:/app" big-data-project
```


## 📊 Generated Insights
After running the container, you will find 7 PNG images in your directory:
1. `age_distribution.png`
2. `age_boxplot.png`
3. `diabetes_distribution.png`
4. `gender_distribution.png`
5. `hypertension.png`
6. `smoking_history.png`
7. `heatmap.png` (Correlation Matrix)

**Developed by:** Team Code X
**Field:** Faculty of Computers and Artificial Intelligence (FCAI)🚀
