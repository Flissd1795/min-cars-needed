def validate_inputs(P, S):
    if not all(isinstance(p, int) and not isinstance(p, bool) for p in P):
        raise TypeError("All values in P must be integers")
    if not all(isinstance(s, int) and not isinstance(s, bool) for s in S):
        raise TypeError("All values in S must be integers")
    if any(p < 0 for p in P):
        raise ValueError("People count cannot be negative")
    if any(s < 0 for s in S):
        raise ValueError("Seat count cannot be negative")