def local(infile, outfile):
    outfile.write(infile.read().encode())
    outfile.close()
    infile.close()

def s_3(client, infile, bucket, file_name):
    client.upload_file(infile, bucket, file_name)
