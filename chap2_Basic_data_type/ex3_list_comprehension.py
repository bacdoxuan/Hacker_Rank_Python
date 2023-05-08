if __name__ == '__main__':
    """
    list all [i,j,k] where 0 <= i <=x, 0 <= j <=y, 0 <= k <=z and i + j + k != n
    x, y, z and n are user's inputs
    """  # NOQA
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in
          range(z + 1) if (i + j + k) != n])
