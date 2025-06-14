import pandas as pd


def display_rows(file_path, num_rows=5):
    """Display the first few rows of the Excel file."""
    for chunk in pd.read_excel(file_path, chunksize=num_rows):
        print(chunk)
        break

def edit_column(file_path, column_name, output_path="edited_output.xlsx", chunk_size=5000):
    """Edit a column in the Excel file in a memory-friendly way."""
    writer = pd.ExcelWriter(output_path, engine="openpyxl")
    first_sheet = True
    for chunk in pd.read_excel(file_path, chunksize=chunk_size):
        print("Current chunk preview:")
        print(chunk.head())
        while True:
            inp = input("Enter row index to edit in this chunk (or 'next' to continue): ")
            if inp.lower() == 'next':
                break
            try:
                idx = int(inp)
                if 0 <= idx < len(chunk):
                    new_val = input(f"New value for {column_name} at row {idx}: ")
                    chunk.loc[idx, column_name] = new_val
                else:
                    print("Index out of range for this chunk.")
            except ValueError:
                print("Invalid input. Provide a numeric index or 'next'.")
        chunk.to_excel(writer, index=False, header=first_sheet)
        first_sheet = False
    writer.close()


def main():
    path = input("Enter path to Excel file: ")
    display_rows(path)
    col = input("Column name to edit: ")
    edit_column(path, col)


if __name__ == "__main__":
    main()
