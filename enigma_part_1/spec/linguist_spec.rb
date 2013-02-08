require 'lib/linguist'

describe Linguist do
  it "should compute the letter frequencies" do
    linguist = Linguist.new
    histogram = linguist.compute_frequencies("EXAMPLEMESSAGE")
    histogram.should == {'E'=>4,'A'=>2,'M'=>2,'S'=>2,'G'=>1,'L'=>1,'P'=>1,'X'=>1}
    histogram = linguist.compute_frequencies("HELLOWORLD")
    histogram.should == {'L'=>3,'O'=>2,'D'=>1,'E'=>1,'H'=>1,'R'=>1,'W'=>1}
  end

  it "should output the letter histogram as PGF/tikz source" do
  end
 
  it "should find the most common digram in the message" do
  end

  it "should find the most common trigram in the message" do
  end
end
