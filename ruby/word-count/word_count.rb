class Phrase
  attr_accessor :content
  attr_reader :assoc_count

  def initialize(content)
    @content = content 
  end

  # Returns a hash with keys as words and number of occurrences as each key's
  # corresponding values.
  def word_count
    words = content.downcase.scan(/\w+(?:'\w+)*/)
    @assoc_count = words.each_with_object(Hash.new(0)) do |word, counts|
      counts[word] += 1 
    end
  end
end

module BookKeeping
  VERSION = 1
end
