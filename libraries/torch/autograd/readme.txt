Each Tensor has a something an attribute called grad_fn, which refers to the
mathematical operator that create the variable. If requires_grad is set to
False, grad_fn would be None. 
