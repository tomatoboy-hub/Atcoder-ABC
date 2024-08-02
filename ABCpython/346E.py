def can_find_sequence_improved(W, B):
    pattern = "wbwbwwbwbwbw"
    # The pattern has 7 white keys and 5 black keys in each cycle.
    cycle_length = 12
    whites_in_cycle = 7
    blacks_in_cycle = 5
    
    # If the demand exceeds the total in a single cycle, it's not possible
    if W > whites_in_cycle or B > blacks_in_cycle:
        return "No"
    
    # Check if the sequence can fit in a single cycle without considering wrap around
    for start in range(cycle_length):
        if start + W + B <= cycle_length:
            # Calculate whites and blacks in this slice
            slice = "wbwbwwbwbwbw" * ((W + B) // cycle_length + 1)  # Extend the pattern to ensure coverage
            whites = slice[start:start+W+B].count('w')
            blacks = slice[start:start+W+B].count('b')
            if whites == W and blacks == B:
                return "Yes"
    
    # If no direct fit is found, consider the wrap around by extending the pattern
    extended_pattern = pattern * 2  # Duplicate pattern to simulate wrap around
    for start in range(cycle_length):
        whites = extended_pattern[start:start+W+B].count('w')
        blacks = extended_pattern[start:start+W+B].count('b')
        if whites == W and blacks == B:
            return "Yes"

    # If none of the checks pass, it's not possible to form such a sequence
    return "No"

# Re-test the logic with corrected approach
W, B = map(int, input().split())
print(can_find_sequence_improved(W,B)) # Should return 'Yes' for the example given earlier
