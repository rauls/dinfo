#!/usr/bin/perl -w

use FCGI;
use File::Slurp;
use File::Copy;
use File::Basename;


# Return kernel information details.
sub GetDataDstat
{
	my $file = "/tmp/dstat." . (rand()*time);
	my $args = shift || "cf";
	my $cmd = "/usr/bin/dstat -$args --float --output $file 1 1 >/dev/null";
	system($cmd);
	my $data = read_file( $file );
	
	unlink $file;
	
	return $data;
}

my $types = {
	cpu =>  { args => "c", title => "CPU" }
};

sub ReturnDstatInfo
{
	my @lines = split( "\n", GetDataDstat() );

	my $header;
	my $data;

	$header = $lines[6];
	$data = $lines[8];
	
	printf( "
{ 
	\"header\": [%s],\n	
	\"data\": [%s] 
}\n", $header, $data );

}

my $request = FCGI::Request();
if($request->Accept() >= 0) {
	print("Content-type: application/json\r\n\r\n");
	ReturnDstatInfo();
}

1;

