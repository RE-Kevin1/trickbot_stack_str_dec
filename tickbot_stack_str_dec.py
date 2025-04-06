from ida_kernwin import ask_str
"""
Function to decrypt stack strings found in a trick bot sample. Just put your at the start of the stack string
"""

def acquire_stack_str(str_start_ea) -> [int]:
    cur_instruction = str_start_ea
    stack_str_int = []
    cur_instruction_mnemonic = print_insn_mnem(cur_instruction)
    while cur_instruction_mnemonic != 'call':
        cur_instruction_mnemonic = print_insn_mnem(cur_instruction)
        if cur_instruction_mnemonic == 'mov':
            dest_op_type = get_operand_type(cur_instruction, 0)
            source_op_type = get_operand_type(cur_instruction, 1)
            if dest_op_type == 4 and source_op_type == 5:
                stack_str_int.append(get_operand_value(cur_instruction, 1))
        cur_instruction = next_head(cur_instruction)
        
    print(stack_str_int)
    return stack_str_int

def dec_stack_str(stack_str: [int]):
    key = stack_str[0]
    dec_str = []
    for i in range(len(stack_str) - 1):
        cur_char = stack_str[i + 1]
        cur_char ^= key
        dec_str.append(chr(cur_char))
    dec_str = "".join(dec_str)
    print(dec_str)
    return dec_str

def dec_stack_str_wrap():
    dec_str = dec_stack_str(acquire_stack_str(here()))
    flag = ask_str("0", 0, "Does this look correct?")
    if flag == "1":
        set_cmt(here(), dec_str, 0)
    
dec_stack_str_wrap()

