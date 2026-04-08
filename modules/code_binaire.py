from modules.bit import Bit
from modules.au_moins_un_bit_erreur import AuMoinsUnBitErreur

class CodeBinaire:
    
    def __init__(self, bit, *bits):
        if not isinstance(bit, Bit):
            raise TypeError("bit must be a Bit")
        self._bits = [bit] + list(bits)
        
    def ajouter(self, bit):
        if not isinstance(bit, Bit):
            raise TypeError("bit must be a Bit")
        self._bits.append(bit)
    
    @property
    def bits(self):
        return tuple(self._bits)
    
    def __str__(self):
        return ''.join(str(bit) for bit in self._bits)
    
    def __repr__(self):
        args = ', '.join(repr(bit) for bit in self._bits)
        return f"CodeBinaire({args})"
    
    def __len__(self):
        return len(self._bits)
    
    def __eq__(self, other):
        if not isinstance(other, CodeBinaire):
            return NotImplemented
        return self._bits == other._bits
    
    def __add__(self, other):
        if not isinstance(other, CodeBinaire):
            raise TypeError("can only concatenate CodeBinaire (not {}) with CodeBinaire".format(type(other).__name__))
        return CodeBinaire(*self._bits, *other._bits)
    
    def __getitem__(self, key):
        if isinstance(key, int):
            return self._bits[key]
        elif isinstance(key, slice):
            return CodeBinaire(*self._bits[key])
        else:
            raise TypeError("indices must be integers or slices")
    
    def __setitem__(self, key, value):
        if isinstance(key, int):
            if not isinstance(value, Bit):
                raise TypeError("value must be a Bit")
            self._bits[key] = value
        elif isinstance(key, slice):
            if isinstance(value, CodeBinaire):
                self._bits[key] = value._bits
            elif hasattr(value, '__iter__') and all(isinstance(b, Bit) for b in value):
                self._bits[key] = list(value)
            else:
                raise TypeError("value must be a CodeBinaire or sequence of Bits")
            if len(self._bits) < 1:
                raise AuMoinsUnBitErreur("CodeBinaire must have at least one bit")
        else:
            raise TypeError("indices must be integers or slices")
    
    def __delitem__(self, key):
        if isinstance(key, int):
            if len(self._bits) <= 1:
                raise AuMoinsUnBitErreur("CodeBinaire must have at least one bit")
            del self._bits[key]
        elif isinstance(key, slice):
            start, stop, step = key.indices(len(self._bits))
            indices = range(start, stop, step)
            num_to_delete = len(indices)
            if len(self._bits) - num_to_delete < 1:
                raise AuMoinsUnBitErreur("CodeBinaire must have at least one bit")
            for i in sorted(indices, reverse=True):
                del self._bits[i]
        else:
            raise TypeError("indices must be integers or slices")
    
    def __iter__(self):
        return iter(self._bits)