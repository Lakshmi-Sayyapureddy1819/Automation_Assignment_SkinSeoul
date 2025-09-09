import pandas as pd
import json

# --- Configuration ---
DATA_FILE = 'Mock_Skincare_Dataset.csv'
OVERRIDE_FILE = 'overrides.json'
OUTPUT_FILE = 'output.json'
TOP_N = 10  # For homepage, top 10 products in carousel

def load_overrides(override_file):
    try:
        with open(override_file, "r") as f:
            data = json.load(f)
            return set(data.get("manual_priority", []))
    except FileNotFoundError:
        return set()

def filter_products(df):
    # Only show in-stock, fast-selling (at least 10 in stock & sold at least once last month)
    filters = (
        (df['Units in Stock'] >= 10) &
        (df['Volume Sold Last Month'] > 0)
    )
    return df[filters].copy()

def score_row(row):
    score = (
        2.0 * row['Volume Sold Last Month'] +      # High sales = most important
        0.2 * row['Views Last Month'] +            # Popularity, but less than sales
        40.0 * (row['Brand Tier'] == 'A') +        # Strong bump for top-tier
        15.0 * (row['Brand Tier'] == 'B') +
        -10.0 * (row['Brand Tier'] == 'C') +       # Slight demote for low-tier
        max(0, (row['Price (USD)'] - row['COGS (USD)'])) # Margin
    )
    return score

def apply_manual_override(df, manual_priority):
    # Items in the override list get the highest possible score +100
    df["Override"] = df["Product Name"].apply(lambda x: x in manual_priority)
    max_score = df['Score'].max() if len(df) > 0 else 1000
    df.loc[df["Override"], "Score"] = max_score + 100
    return df

def main():
    # Load data
    df = pd.read_csv(DATA_FILE)
    
    # Filtering
    filtered = filter_products(df)
    
    # Scoring
    filtered["Score"] = filtered.apply(score_row, axis=1)
    
    # Manual override (e.g. new launches)
    manual_priority = load_overrides(OVERRIDE_FILE)
    filtered = apply_manual_override(filtered, manual_priority)
    
    # Sort and take top N
    filtered = filtered.sort_values(by=["Score", "Volume Sold Last Month"], ascending=[False, False])
    top_products = filtered.head(TOP_N)
    
    # Output to JSON (frontend ready)
    result = top_products.to_dict(orient='records')
    with open(OUTPUT_FILE, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Top {TOP_N} products saved to {OUTPUT_FILE}")

    # Optional: CSV output
    top_products.to_csv('output.csv', index=False)
    print("CSV output written to 'output.csv'.")

if __name__ == "__main__":
    main()
