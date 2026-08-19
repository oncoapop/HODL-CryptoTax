import math
from importer import import_csvs
from acb import get_yearly_reconciliation

expected_milestones = {
    '2020': {'Proceeds': 21352.69, 'ACB': 18709.61, 'Gain': 2643.08},
    '2021': {'Proceeds': 61346.96, 'ACB': 55824.90, 'Gain': 5522.06},
    '2022': {'Proceeds': 15924.68, 'ACB': 13506.24, 'Gain': 2418.44},
    '2023': {'Proceeds': 57064.60, 'ACB': 60284.66, 'Gain': -3220.06},
    '2024 P1': {'Proceeds': 18927.99, 'ACB': 17122.81, 'Gain': 1805.18},
    '2024 P2': {'Proceeds': 18402.09, 'ACB': 27937.29, 'Gain': -9535.19},
    '2025': {'Proceeds': 5648.72, 'ACB': 7546.05, 'Gain': -1897.33},
}

def run_tests():
    print("Starting CytoTax Reconciliation...")
    import_csvs()
    print("Computing ACB and Proceeds...")
    results = get_yearly_reconciliation()
    
    print("\n--- RECONCILIATION REPORT ---")
    all_passed = True
    for year, expected in expected_milestones.items():
        actual = results.get(year, {'Proceeds': 0.0, 'ACB': 0.0, 'Gain': 0.0, 'Income': 0.0})
        
        dp = actual['Proceeds'] - expected['Proceeds']
        da = actual['ACB'] - expected['ACB']
        dg = actual['Gain'] - expected['Gain']
        
        print(f"\nYear {year}:")
        print(f"  Proceeds: Expected {expected['Proceeds']:>10.2f} | Actual {actual['Proceeds']:>10.2f} | Delta {dp:>8.2f}")
        print(f"  ACB:      Expected {expected['ACB']:>10.2f} | Actual {actual['ACB']:>10.2f} | Delta {da:>8.2f}")
        print(f"  Gain:     Expected {expected['Gain']:>10.2f} | Actual {actual['Gain']:>10.2f} | Delta {dg:>8.2f}")
        print(f"  [Info] Income tracked: {actual.get('Income', 0.0):.2f}")
        
        if abs(dp) > 5.0 or abs(da) > 5.0 or abs(dg) > 5.0:
            print(f"  -> WARNING: {year} exceeds $5.00 tolerance!")
            all_passed = False
        else:
            print(f"  -> {year} RECONCILED OK.")
            
    if all_passed:
        print("\nSUCCESS: All years reconciled within tolerance.")
    else:
        print("\nFAILURE: Some years failed reconciliation. Check deltas.")
        
if __name__ == '__main__':
    run_tests()
