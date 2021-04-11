import socket
import base64
from PIL import Image
import sys
import random
from PIL import ImageFile

def findnumberofTriangles(arr): 
  
    # Sort array and initialize count as 0 
    n = len(arr) 
    arr.sort() 
    count = 0
  
    # Fix the first element. We need to run till n-3 as 
    # the other two elements are selected from arr[i+1...n-1] 
    for i in range(0,n-2): 
  
        # Initialize index of the rightmost third element 
        k = i + 2
  
        # Fix the second element 
        for j in range(i+1,n): 
  
            # Find the rightmost element which is smaller 
            # than the sum of two fixed elements 
            # The important thing to note here is, we use 
            # the previous value of k. If value of arr[i] + 
            # arr[j-1] was greater than arr[k], then arr[i] + 
            # arr[j] must be greater than k, because the array 
            # is sorted. 
            while (k < n and arr[i] + arr[j] > arr[k]): 
                k += 1
  
            # Total number of possible triangles that can be 
            # formed with the two fixed elements is k - j - 1. 
            # The two fixed elements are arr[i] and arr[j]. All 
            # elements between arr[j+1] to arr[k-1] can form a 
            # triangle with arr[i] and arr[j]. One is subtracted 
            # from k because k is incremented one extra in above 
            # while loop. k will always be greater than j. If j 
            # becomes equal to k, then above loop will increment k, 
            # because arr[k] + arr[i] is always greater than arr[k] 
            if(k>j): 
                count += k - j - 1
  
    return count 

# arr = [i for i in range(1,6)]
# print(findnumberofTriangles(arr))


def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    # s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    while(1):
        chunk = s.recv(4096)
        n = int(chunk.decode('utf-8').split()[-2])
        print(n)
        arr = [i for i in range(1,n+1)]
        ans = findnumberofTriangles(arr)
        s.sendall(bytes(str(ans) + '\n', 'utf-8'))
    # chunk = s.recv(4096)
    # print(chunk.decode('utf-8'))
    print("Connection closed.")
    s.close()

host = '15.164.75.32'
port = 1999

netcat(host, port)