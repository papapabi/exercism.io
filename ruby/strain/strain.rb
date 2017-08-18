module Enumerable
  def keep(&block)
    if block_given?
      [].tap { |result| each { |e| yield(e) ? result << e : nil } }
    else 
      enum_for(:keep) { size }
    end
  end

  def discard(&block)
    if block_given?
      [].tap { |result| each { |e| yield(e) ? nil : result << e } }
    else 
      enum_for(:discard) { size }
    end
  end
end
