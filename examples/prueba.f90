program prueba

    implicit none
    integer :: i
    real :: x
    
    x = 0.0
    do i = 1, 10
         x = x + 1.0 / real(i)
    end do
    
    print *, "La suma de los primeros 10 terminos de la serie armonica es:", x
    print *, "Fin del programa."
end program prueba