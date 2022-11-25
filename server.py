from flask import Flask, render_template, request
import boto3
import sys



app = Flask(__name__)
s3 = boto3.resource("s3")

bucket = s3.Bucket(sys.argv[1])




@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    photo = request.files.get("photo", "")
    print(photo)
    object = bucket.put_object(
        Body = photo,
        Key = photo.filename
    )
    print(object)
    return {"msg": "Uploaded successfully"}







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False )