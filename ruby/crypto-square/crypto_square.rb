class Crypto
  attr_reader :ciphertext, :plaintext

  def initialize(text)
    @plaintext = text
    @ciphertext = to_cipher(text)
  end

  def to_cipher(text)
    return "" if text.empty?
    normalized = normalize(text)
    rectangle_words = rectangle_words(normalized)
    rectangle_chars = rectangle_words.map(&:chars)
    first_chars = rectangle_chars.shift
    cipher_words = first_chars.zip(*rectangle_chars).map(&:join)
    append_whitespace(cipher_words).join(" ")
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

  def rectangle_words(normalized)
    c = find_c(normalized.length)
    normalized.chars.each_slice(c).map(&:join)
  end

  # Only c is needed for this solution.
  def find_c(string_length)
    Math.sqrt(string_length).ceil
  end

  # Concatenates whitespace to the end of each word in the array given to
  # 'regularize' the lengths to max_length.
  def append_whitespace(arr_words)
    max_length = arr_words.map(&:size).max
    arr_words.map do |word|
      next if word.length == max_length
      word = (max_length - word.size).times { word << " " }
    end
    arr_words
  end

  private :to_cipher, :normalize, :remove_whitespace, 
    :remove_punctuations, :rectangle_words, :find_c
end

module BookKeeping
  VERSION = 1
end
