class Crypto
  attr_reader :ciphertext, :plaintext

  def initialize(text)
    @plaintext = text
    @ciphertext = to_cipher(text)
  end

  def to_cipher(text)
    return "" if text.empty?
    normalized = normalize(text)
    rectangle_words = compute_rectangle(normalized)
    rectangle_chars = rectangle_words.map(&:chars)
    first_chars = rectangle_chars.shift
    first_chars.zip(*rectangle_chars).map(&:join).join(" ")
  end

  def normalize(s)
    no_space = remove_whitespace(s)
    no_punct = remove_punctuations(no_space)
    no_punct.downcase
  end

  def remove_whitespace(s)
    s.gsub(/\s+/, "")
  end

  def remove_punctuations(s)
    s.gsub(/\p{P}/, "")
  end

  def compute_rectangle(normalized)
    c = find_c(normalized.length)
    normalized.chars.each_slice(c).map(&:join)
  end

  # Only c is needed for this solution.
  def find_c(string_length)
    Math.sqrt(string_length).ceil
  end

  private :to_cipher, :normalize, :remove_whitespace, 
    :remove_punctuations, :compute_rectangle, :find_c
end

module BookKeeping
  VERSION = 1
end
