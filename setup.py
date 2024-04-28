from setuptools import setup, find_packages

setup(
    name='FastqToFastaConverter',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    author='Edris Sharif Rahmani',
    author_email='rahmani.biotech@gmail.com',
    description='FastQ to FASTA file converter',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sharifrahmanie/FastqToFastaConverter/archive/refs/tags/v0.1.tar.gz',
    keywords=['FASTQ', 'FASTA','Bioinformatics'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
