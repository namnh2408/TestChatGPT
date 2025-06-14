# TestChatGPT

Testing Codex ChatGPT with Github

## Excel App

`excel_app.py` provides a basic command line interface to inspect large Excel files
and edit values in a selected column. The script uses chunked reading via
`pandas` so it can handle very large spreadsheets without loading everything
into memory at once.

### Usage

1. Make sure `pandas` and `openpyxl` are installed.
2. Run the script:

```bash
python excel_app.py
```

3. Enter the path to your Excel file when prompted. The script will show a
   preview of the first few rows.
4. Provide the column name you want to edit. For each chunk of rows, you can
   choose row indices to modify or type `next` to move on.
5. The edited file is saved as `edited_output.xlsx` in the current directory.
