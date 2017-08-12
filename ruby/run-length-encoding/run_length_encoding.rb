class RunLengthEncoding
  def self.encode(s)
    # Array#chunk returns the a) return value of the block, and
    # b) chunked elements based from the return value, which are 
    # char and ar respectively.
    s.chars.chunk { |c| c }.reduce("") do |encoding, (char, chunked)|
      if chunked.length == 1
        encoding << char
      else
        encoding << "#{chunked.length}" + char
      end
    end
  end

  def self.decode(s)
    # String#scan returns an array of all matches given the regex as its
    # argument, which is then unfolded by the 2nd block variable to reduce.
    s.scan(/(\d+)*(.)/).reduce("") do |decoding, (count, char)|
      if count.nil?
        decoding << char
      else
        decoding << char*Integer(count)
      end
    end
  end
end

module BookKeeping
  VERSION = 3
end
