/* TTDecomp - file decompression for 'TTComp archive data'
   Copyright (C) 2012 Tony Lewis <tlewis@exelana.com>

   Version: 1.0

TTDecomp is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

TTDecomp is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Wget.  If not, see <http://www.gnu.org/licenses/>.

Additional permission under GNU GPL version 3 section 7 */

/* The following files are from the Starcraft/Brood War Library:
   - implode.c
   - common.c
   - common.h

   Found online at http://code.google.com/p/lawine/

   License: GNU Lesser GPL
*/

/* The file posix.h was created to so that implode.c would compile
   on a Unix machine. */

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#ifdef WIN32
#pragma warning (disable : 4996)
#include <windows.h>
#endif

#include "implode.h"

#define VERSION "1.0"

#ifdef WIN32
int _tmain(int argc, _TCHAR* argv[])
#else
int main (int argc, char** argv)
#endif
{
  unsigned char *in_buffer, *out_buffer;
  size_t in_buffer_size, out_buffer_size;
  unsigned int exploded_size;
  FILE *in_file, *out_file;
#ifdef WIN32
  char in_path[MAX_PATH], out_path[MAX_PATH];
#else
  char *in_path, *out_path;
#endif
  unsigned int n_bytes_read, n_bytes_written;
  struct stat st;

  if (argc < 3)
  {
    printf("ttdecomp: decompress 'TTComp archive data'\n");
    printf("Version: %s\n\n", VERSION);
    printf("Usage: ttdecomp inpath outpath\n");
    exit(1);
  }
#ifdef WIN32
  sprintf(in_path, "%ws", argv[1]);
  sprintf(out_path, "%ws", argv[2]);
#else
  in_path = argv[1];
  out_path =argv[2];
#endif

  if (stat(in_path, &st))
  {
    fprintf(stderr, "ttdecomp: Unable to get size of file %s; %s\n", in_path, strerror(errno));
    exit(1);
  }

  in_buffer_size = st.st_size;
  in_buffer = (unsigned char *)malloc(in_buffer_size);
  if (in_buffer == NULL)
  {
    fprintf(stderr, "ttdecomp: Unable to allocate buffer to read file %s; need %zd bytes\n",
      in_path, in_buffer_size);
    exit(1);
  }

  in_file = fopen(in_path, "rb");
  if (in_file == NULL)
  {
    fprintf (stderr, "ttdecomp: Couldn't open file %s; %s\n", in_path, strerror (errno));
    exit(1);
  }

  n_bytes_read = fread(in_buffer, 1, in_buffer_size, in_file);
  if (n_bytes_read < 4 || in_buffer[0] != 0x00 || in_buffer[1] != 0x06)
	{
    fprintf (stderr, "ttdecomp: %s does not appear to be a TTCOMP archive\n", in_path);
    exit(1);
  }

  out_buffer_size = in_buffer_size * 16; // allow plenty of room for decompression
  out_buffer = (unsigned char *)malloc(out_buffer_size);
  if (out_buffer == NULL)
  {
    fprintf(stderr, "ttdecomp: Unable to allocate buffer to decompress file %s\n", in_path);
    exit(1);
  }

  exploded_size = out_buffer_size;
  if (!explode(in_buffer, n_bytes_read, out_buffer, &exploded_size))
  {
    fprintf(stderr, "ttdecomp: Unable to decompress file %s\n", in_path);
    exit(1);
  }
  if (exploded_size > out_buffer_size)
  {
    fprintf(stderr, "ttdecomp: Decompressed data is larger than allocated buffer: %d > %zd\n",
      exploded_size, out_buffer_size);
    exit(1);
	}

  out_file = fopen(out_path, "wb");
  if (out_file == NULL)
  {
    fprintf (stderr, "ttdecomp: Couldn't open file %s; %s\n", out_path, strerror (errno));
    exit(1);
  }

  n_bytes_written = fwrite(out_buffer, 1, exploded_size, out_file);
  if (n_bytes_written < exploded_size)
  {
    fprintf (stderr, "ttdecomp: Failed to write to file %s; %s\n", out_path, strerror (errno));
    exit(1);
  }

  fclose(in_file);
  fclose(out_file);
  exit(0);
}
