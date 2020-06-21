def local(infile, outfile):
    infile_read = infile.read()
    try:
        outfile.write(infile_read)
    except TypeError:
        try:
            outfile.write(infile_read.encode())
        except AttributeError:
            outfile.write(infile_read.decode())
    outfile.close()
    infile.close()

def s_3(client, infile, bucket, file_name):
    client.upload_fileobj(infile, bucket, file_name)
