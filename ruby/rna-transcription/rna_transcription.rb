class Complement
  DNA_TO_RNA = { "G" => "C", "C" => "G", "T" => "A", "A" => "U" }
  def self.of_dna(dna)
    return '' if dna =~ /[^GCTA]+/
    dna.gsub(/[GCTA]/, DNA_TO_RNA) 
  end
end
