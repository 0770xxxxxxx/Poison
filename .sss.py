#Encrypt by MAHADI HASAN AFRIDI
#Github : https://github.com/MAHADI-143
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))