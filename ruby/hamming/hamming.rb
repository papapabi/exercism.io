class Hamming
  def self.compute(dna_string, other_dna_string)
    hamming_difference = 0
    dna_string.chars.zip(other_dna_string.chars).each do |c, o_c|
      hamming_difference += 1 if c != o_c
    end
    hamming_difference
  end
end
