.data

	array:		 .word 3 , 7 , 5 , 2
	lungimearr:  .space 16
	i:			 .word 0
	k:			 .word 0	
	n:			 .word 4
	adunarecu4:  .word 0
.text

main:

	
	lw	$t0, k	
	lw	$t1, k
	la	$t4, array
	lw	$t5, n
	
	j etichetaForI

	etichetainterschimbare:
	
	# t2 = t8
	# t3 = t9
	add		$t8, $t8, $t9
	sub		$t9, $t8, $t9
	sub		$t8, $t8, $t9
	
	sw	 $t8, 0($t2)
	sw	 $t9, 0($t3)

	j etichetaReia

	lw	$s4, k
	
	etichetaForI:
		
		move $t1, $t0

		  etichetaForKNenul:
			
			move $t6, $t0 
			sll	$t6, $t6, 2 # i*=4
			add $t2, $t4, $t6 #v[i]
			lw	$t8, 0($t2)	

			move $t7, $t1
			sll  $t7, $t7, 2 # j*=4
			add	 $t3, $t4, $t7 #v[j]
			lw	 $t9, 0($t3)

			bgt	$t8, $t9, etichetainterschimbare
				
				etichetaReia:
					addi $t1, 1 # t1 = k = 1
					blt $t1, $t5, etichetaForKNenul
					addi $t0, 1 #to = 1
					blt $t0, $t5, etichetaForI
					j etichetaExit

etichetaExit:

li $v0,10

syscall