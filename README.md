# SkinSeoul AI Agent Automation Engineer Case Study

## Overview

This project is a data-driven, fully automated merchandising system for SkinSeoul’s e-commerce homepage "Best Sellers" carousel. The solution dynamically ranks and curates products using business and analytics logic, and includes a manual override layer for marketing and campaign flexibility.

---

## Folder Contents

- `products.csv` - Mock skincare product analytics dataset.
- `overrides.json` - Optional list of manually prioritized product names.
- `product.py` - Main Python logic to filter, score, and rank best sellers.
- `homepage_best_sellers.json` - Output file of top N ranked products (frontend ready).
- `homepage_best_sellers.csv` - CSV output for reference/analytics.
- `README.md` - This documentation file.
- `assignment.pdf` - 2-page deliverable outlining rationale, logic, and a flow diagram.
- `presentation.mp4` - (Optional/video) 2-minute explainer video.

---

## How It Works

1. **Data Ingestion**: Loads product analytics from `products.csv` and any manual overrides from `overrides.json`.  
2. **Filtering**: Only considers products in stock (>=10 units) and with at least one sale last month.  
3. **Scoring**: Ranks products using a weighted formula factoring in sales, popularity, brand tier, and profit margin.  
4. **Manual Override Layer**: Any product in `overrides.json` is promoted to the top of the recommendations, enabling instant business control.  
5. **Output**: Exports the top N products (default 10) to `homepage_best_sellers.json` (for the frontend) and `homepage_best_sellers.csv`.  

---

## Files Explained

- **products.csv**  
  Contains the following fields for each product:  
  - Product Name  
  - Brand  
  - Brand Tier  
  - Price (USD)  
  - COGS (USD)  
  - Days of Inventory  
  - Units in Stock  
  - Views Last Month  
  - Volume Sold Last Month  

- **overrides.json**  
  Example:  
  ```json
  {
    "manual_priority": [
      "Glow Niacinamide Mask",
      "Fresh Niacinamide Cream"
    ]
  }
  ```  
  Any product listed here will appear at the very top of the Best Sellers list.

- **product.py**  
  Main script. Reads the CSV & JSON, filters, applies business scoring (see assignment.pdf for details), applies overrides, and outputs ranked results for the homepage.

---

## Usage

1. **Requirements**  
   - Python 3  
   - pandas  

2. **Run the Script**  
   ```bash
   python product.py
   ```

3. **Outputs**  
   - `homepage_best_sellers.json` (Top N products for frontend carousel)  
   - `homepage_best_sellers.csv` (For review/analytics)  

---

## Scoring Logic

For each product:  

```
Score = 2.0 * (Volume Sold Last Month)
      + 0.2 * (Views Last Month)
      + 40 (if Tier A)
      + 15 (if Tier B)
      - 10 (if Tier C)
      + max(0, Price - COGS)
```

- Manual override via `overrides.json` ensures key SKUs are always shown.

---

## Diagram

See `assignment.pdf` for the full automation process map.

---

## Assignment Deliverables

- 2-page PDF writeup (touchpoint rationale, logic, diagram)  
- .mp4 video summary (optional)  
- Source code & small data files  

---

## Contact

For questions or discussion, please reach out to **your.email@domain.com**.

---

**Thank you for reviewing my solution!**
