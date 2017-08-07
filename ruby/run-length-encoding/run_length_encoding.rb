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
  end
end

module BookKeeping
  VERSION = 3
end
