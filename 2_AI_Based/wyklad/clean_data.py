import csv
import re

def is_empty_row(row):
    """Check if a row is completely empty (all fields are empty/None)"""
    return all(not value or value.strip() == '' for value in row.values())

def has_minimum_data(row):
    """Check if row has minimum required data (at least locality or street)"""
    locality = row.get('locality', '').strip() if row.get('locality') else ''
    street = row.get('street', '').strip() if row.get('street') else ''
    return bool(locality or street)

def clean_value(value):
    """Clean and normalize a single value"""
    if not value:
        return None
    value = value.strip()
    return value if value else None

def clean_numeric(value):
    """Clean numeric value, return None if empty"""
    if not value or not value.strip():
        return None
    cleaned = re.sub(r'[^\d]', '', str(value).strip())
    return cleaned if cleaned else None

def clean_owner_type(owner_type):
    """Normalize owner_type field"""
    if not owner_type:
        return None
    owner_lower = owner_type.lower()
    if 'pośrednik' in owner_lower or 'bez pośredników' in owner_lower:
        return 'Bez pośredników'
    elif 'biura nieruchomości' in owner_lower or 'biuro nieruchomości' in owner_lower:
        return 'Oferta biura nieruchomości'
    return owner_type.strip()

def clean_date_posted(date_posted):
    """Normalize date_posted field"""
    if not date_posted:
        return None
    date = date_posted.strip()
    # Normalize some common variations
    if date == 'dzisiajnowe':
        return 'dzisiaj'
    elif date == 'wczorajnowe':
        return 'wczoraj'
    return date

# Input and output files
input_file = "mieszkania_warszawa.csv"
output_file = "mieszkania_warszawa_cleaned.csv"

cleaned_rows = []
rows_removed = 0

# Read and clean the data
with open(input_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    
    for row_num, row in enumerate(reader, start=2):  # Start at 2 (header is row 1)
        # Skip completely empty rows
        if is_empty_row(row):
            rows_removed += 1
            continue
        
        # Skip rows without minimum required data
        if not has_minimum_data(row):
            rows_removed += 1
            continue
        
        # Clean each field
        cleaned_row = {}
        for field in fieldnames:
            value = row.get(field, '')
            
            # Special cleaning for specific fields
            if field in ['rooms', 'area', 'price_total_zl', 'price_sqm_zl', 'photo_count']:
                cleaned_row[field] = clean_numeric(value)
            elif field == 'owner_type':
                cleaned_row[field] = clean_owner_type(value)
            elif field == 'date_posted':
                cleaned_row[field] = clean_date_posted(value)
            else:
                cleaned_row[field] = clean_value(value)
        
        cleaned_rows.append(cleaned_row)

# Write cleaned data to new file
if cleaned_rows:
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)
    
    print(f"✓ Cleaning complete!")
    print(f"  Original rows: {rows_removed + len(cleaned_rows)}")
    print(f"  Rows removed: {rows_removed}")
    print(f"  Clean rows: {len(cleaned_rows)}")
    print(f"  Output saved to: {output_file}")
else:
    print("No valid data found after cleaning.")

