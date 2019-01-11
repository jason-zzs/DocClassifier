with open('CT-283782.csv', 'r') as src_file:
    out_file = open('training_data.csv', 'w')
    num_lines = 0
    
    for line in src_file:
        num_lines += 1
			
        if ('0' <= line[0] <= '9') and line.rstrip()[-1] == ',':
            if '.jpg' in line or '.png' in line or '?xml' in line or '469365' in line:
                src_file.readline()
            else:
                out_file.write(line.rstrip()[:-2])
		
        elif '0' <= line[0] <= '9':
            if '.jpg' in line or '.png' in line or '?xml' in line or '469365' in line:
                continue
				
            out_file.write(line)
			
        else:
            if line[0] != '"' and num_lines > 1:
                index = line.rfind(',"')
                line = line[:index] + '"' + line[index:]
                
            out_file.write(line.lstrip('"').replace(',,,,', ''))
			
    out_file.close()
