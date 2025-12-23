# Vehicle Recovery Handwritten Note OCR Web App

This project is a Streamlit web application designed for vehicle recovery companies that record daily jobs on handwritten notepads. The app uses Google Cloud Vision OCR to extract structured information from photos of these notes, making it easy to digitize and manage job records.

## Features

- **Handwritten OCR:** Uses Google Cloud Vision API to recognize handwritten Turkish notes from images.
- **Webcam Integration:** Capture a photo of the notepad directly from your webcam or upload an image file.
- **Automatic Field Extraction:** Extracts and fills the following fields automatically:
  - Date
  - Time
  - Cargo Company Name
  - Vehicle Plate Number
  - Route Description (from/to)
  - File Number
  - Contact Phone Number
- **Editable Fields:** All extracted fields are displayed in editable text boxes for manual correction.
- **Data Validation:** Ensures all required fields are filled before allowing database submission.
- **Database Integration:** Save the corrected and validated data to a database with a single click.
- **Excel Export:** Optionally, export the records to an Excel file for further processing.

## How It Works

1. **Capture or Upload Image:** Take a photo of the handwritten note using your webcam or upload an existing image.
2. **OCR Processing:** The app processes the image using Google Cloud Vision and extracts relevant fields.
3. **Review & Edit:** The extracted information is displayed in text fields. You can review and edit any field as needed.
4. **Save to Database:** Once all fields are complete and correct, click the "Save" button to store the record in the database.
5. **Export:** Optionally, export the data to Excel.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/mutithegreat/handwrite_recognition.git
   cd handwrite_recognition
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Set up Google Cloud Vision:**
   - Create a Google Cloud project and enable the Vision API.
   - Create a service account and download the JSON key file.
   - Set the environment variable for authentication:
     ```
     set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\service-account.json
     ```

4. **Run the app:**
   ```
   streamlit run app.py
   ```

## Requirements

- Python 3.8+
- streamlit
- google-cloud-vision
- pandas
- pillow
- opencv-python

(See `requirements.txt` for the full list.)

## Usage

- Open the web app in your browser.
- Capture or upload a notepad image.
- Review and edit the extracted fields.
- Click "Save" to store the data in the database.
- Optionally, export to Excel.

## Notes

- The accuracy of OCR depends on the quality and clarity of the handwritten notes.
- Manual correction is recommended for best results.
- The app is designed for Turkish handwritten notes but can be adapted for other languages.

## License

MIT License

---

**Developed for vehicle recovery companies to digitize handwritten job records efficiently.**