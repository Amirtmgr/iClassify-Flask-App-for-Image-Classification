

# File types
FILE_TYPES = set(['png', 'jpg', 'jpeg'])

# Check file type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES