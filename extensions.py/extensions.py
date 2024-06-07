def main():
   file_type=input("File name:").strip()
   if file_type.endswith(".gif"):
        print("image/gif")
   elif file_type.endswith(".jpg"):
        print("image/jpeg")
   elif file_type.endswith(".zip"):
        print("application/zip")
   elif file_type.endswith(".png"):
        print("image/png")
   elif file_type.endswith(".PDF"):
        print("application/pdf")
   elif file_type.endswith(".txt"):
        print("text/plain")
   elif file_type.endswith(".jpeg"):
        print("image/jpeg")
   elif file_type.endswith(".pdf"):
        print("application/pdf")
   elif file_type.endswith(".txt.pdf"):
        print("application/pdf")
   else: print("application/octet-stream")
main()
