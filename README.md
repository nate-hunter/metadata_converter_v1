# DJANGO FILE UPLOAD DEMO

## BASIC CONCEPTS:
- Send file using POST request
- Set proper form encode type
	* enctype="multipart/form-data"
- Files are uploaded to request.FILES
	* Dictionary-like object
	* Each file is an UploadedFile instance

## CONFIGURATION:
- MEDIA_ROOT
- MEDIA_URL
- Serving media files on local machine

## HANDLING UPLOADED FILES
- File storage API - FileSystemStorage
- Model form fields FileField and ImageField
	* FileField
		- File saved in the file system
		- Saved as text in the database
		- File is not deleted if object is deleted
		- Override model delete method
	* ImageField
		- Pillow -- Pillow (PIL Fork) 5.3.0 documentation





