# CopyMoveFile
PYTHON GUI TO COPY OR MOVE FILES FROM ONE DIRECTORY TO ANOTHER DIRECTORY USING THE shutil MODULE

The shutil module offers a number of high-level operations on files and collections of files.In particular, functions are provided which support file copying and removal.

shutil.copy(src, dst, *, follow_symlinks=True) - Copies the file src to the file or directory dst.src and dst should be strings. If dst specifies a directory, the file will be copied into dst using the base filename from src. Returns the path to the newly created file.

shutil.move(src, dst, copy_function=copy2) - Recursively move a file or directory (src) to another location (dst) and return the destination.

