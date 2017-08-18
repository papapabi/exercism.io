module Enumerable
  def keep(&block)
    result = []
    if block_given?
      each do |e|
        if yield(e)
          result << e
        end
      end
    else 
      each do |e| 
        if block.call(e)
          result << e
        end
      end
    end
    result
  end

  def discard(&block)
    result = []
    if block_given?
      each do |e|
        unless yield(e)
          result << e
        end
      end
    else
      each do |e|
        unless block.call(e)
          result << e
        end
      end
    end
    result
  end
end
