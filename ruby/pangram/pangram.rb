require 'set'

class Pangram
  def self.pangram?(phrase)
    alphabet = ('a'..'z').to_set
    normalized_phrase = phrase.downcase.chars.to_set
      .keep_if { |c| letter?(c) }
    alphabet == normalized_phrase 
  end
  def self.letter?(lookAhead)
    lookAhead =~ /[[:alpha:]]/
  end
  private_class_method :letter?
end
