import sys
import binascii


#@brief Convert an int to bytes with default byte order
#@param int 
#@return byte
#@note only convert the lower byte of the integer
def NumberToBytes(number):
    return number.to_bytes(1,sys.byteorder)

#@brief Convert an int lower byte to byte array
#@param int 
#@return bytearray
#@warning only convert the lower byte of the integer!
def NumberToByteArray(number):
    return bytearray(number.to_bytes(1,sys.byteorder))


#@brief Print a bytearray in 'readable' form
#@param bytearray 
#@note using binascii
def PrintByteArray(byte_array):
    print(binascii.hexlify(byte_array))
