stubs_py3
=========

Standard bioinformatics pipelining stubs for Python (3) scripting (used by me, if none else). Implementing some tricks stumbled upon on the internet; providing a [Apache 2.0] + [CC BY 4.0] licensing system suitable for scientific programming.

For your own ease of use; please fork and update with your own name and current year in license information.

Provided under [MIT license] to enable the least legal friction in sharing of these stubs.

## IANAL Disclaimer

I am not a lawyer - therefore nothing stated in this file is to be taken as legal advice.

## Description of stock stubs
 
### stub_main_only_*.py
Simple but older stub that takes some command line arguments using argparse.

Main trick for library dual-acting.

### stub_reading_file_or_stdin_*.py
Stub as above, GNU-style; reading either from STDIN or from a list of files, thus enabling seamless shell piping to and from scripts on command line.

## License of stubs

These code stubs are provided under the [MIT license]; the license information within the stubs themselves are to be removed or altered in any way the licensee see fit - as these licenses are only stock examples.

Thus you are free to use these stubs, adapt them to your own work, in any manner that the MIT license enables; which means you can drop the MIT license all together, without having to copyright reference the author of the stubs, and start using any of the other licenses in the stubs for your own projets with your own name and organizations - since derivative works of MIT Licensed software can be distributed under other licenses.

The stock licenses are;

* `*_gpl.py`, [GNU GPL v3]
* `*_a2.py`, [Apache 2.0], using recommended [Apache boilerplate].

Include, rename and reformat `NOTICE_example.a2` together with the `LICENSE_ccby.html` for [CC BY 4.0] licensing of documentation and example materials.

## How to use licenses in own work (Apache 2.0 + CC BY 4.0)

The [Apache 2.0] license is a good license providing both options for downstream copyrighted and copylefted derivative work. Since Apache 2.0 also support a [NOTICE] system, wherein **proper attribution (citing) in scientific journal publications can be defined**, the Apache 2.0 is the license I've found is the most suitable for scientific programming.

Although a lengthy NOTICE file is generally considered a downstream [burden], according to Apache 2.0 license documentation, for scientific programming and publication proper referencing is instead considered a general nescessity.

Just change the copyright notices of your choice to the relevant year, project name and your (or your orgs) name; and edit the `NOTICE_example.a2` into your liking, should you go with the provided Apache 2.0 + CC BY 4.0 system.

### CC BY 4.0

All documentation, examples and other promotion material provided by the author(s) are licensed under [CC BY 4.0], with attribution guidelines provided in the Apache 2.0 NOTICE file.

[apache 2.0]: https://www.apache.org/licenses/LICENSE-2.0.html
[apache boilerplate]: http://apache.org/licenses/LICENSE-2.0.html#apply
[notice]: http://www.apache.org/licenses/LICENSE-2.0.html#redistribution
[burden]: http://www.apache.org/dev/licensing-howto.html#mod-notice
[cc by 4.0]: https://creativecommons.org/licenses/by/4.0/
[gnu gpl v3]: https://www.gnu.org/licenses/gpl-3.0.en.html
[mit license]: https://opensource.org/licenses/MIT
