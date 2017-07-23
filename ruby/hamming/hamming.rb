class Hamming
  class << self
    def compute(dna_string, other_dna_string)
      unless dna_string.length == other_dna_string.length
        raise ArgumentError.new('Strings must be of equal length')
      end
      dna_string.chars.zip(other_dna_string.chars).count { |c, o_c| c != o_c }
    end
  end
end

module BookKeeping
  VERSION = 3
end

