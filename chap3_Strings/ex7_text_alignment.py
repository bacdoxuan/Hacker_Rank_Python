if __name__ == '__main__':
    """
    draw hackerrank icon with input thickness.
    Example:
    thickess = 5
    output:
        H    
       HHH   
      HHHHH  
     HHHHHHH 
    HHHHHHHHH
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHHHHHHHHHHHHHHHHHHHHHH   
      HHHHHHHHHHHHHHHHHHHHHHHHH   
      HHHHHHHHHHHHHHHHHHHHHHHHH   
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHH               HHHHH             
      HHHHH               HHHHH             
                        HHHHHHHHH 
                         HHHHHHH  
                          HHHHH   
                           HHH    
                            H   
    """  # NOQA

    thickness = int(input())  # This must be an odd number
    c = 'H'

    # Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    # Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))  # NOQA

    # Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    # Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))  # NOQA

    # Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))  # NOQA
