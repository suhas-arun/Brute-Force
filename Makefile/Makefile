CC = g++
PY = python3
CPPTARGET = generate_data
PYTARGET = plot

all:	generate plot clean

generate:
		$(CC) ${CPPTARGET}.cpp -o ${CPPTARGET}
		./${CPPTARGET}

plot:
		$(PY) ${PYTARGET}.py

clean:
		rm  data.txt