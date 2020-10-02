"""
https://start.interviewing.io/showcase/groqRn7wWK4e

An online service exists that lets users install packages and their dependencies
on their computer. This service tracks "Package" objects, which have a name,
version, size, and license. Packages can depend on other Packages.

Your goal is to write a library, made up of one or more classes, that given a
Package name and version can answer queries about that Package. For now support
three queries. Write your library in a way that supports adding additional
queries on new package properties in a maintainable way.

1. Check if the package's total installed size (Package size + all dependency
   Package sizes) is > XYZ MB.
2. Check if the package depends on a specific package name and version, either
   directly or transitively.
3. Check if the package's license, or any of their dependency licenses, match a
   configurable blocklist of undesired licenses e.g. {"GPL 3", "GPL 2",
   "Creative Commons"}.

You have access to a class "PackageApi" that has a method `Package
getPackage(String packageName, String packageVersion)` that can return a
package.

You can solve this question in any programming language you like. Here are some
Java-like classes as reference for what you have available to you, but you can
convert these / assume they exist in your chosen language:

class PackageApi {
    Package getPackage(String packageName, String packageVersion) { ... }
}

class Package {
    String getName() { ... }
    String getVersion() { ... }
    String getLicense() { ... }
    long getSizeBytes() { ... }
    List<Package> getDependencies() { ... }
}
"""


class PackageLibrary:
    
    def __init__(self, packageName, version):
        self.startingPackage = getPackage(packageName, version)


    def packageSizeGreaterThan(self, xyz):
        stack = [self.startingPackage]
        seen = set([self.startingPackage])
        size = 0
        while stack:
            currPackage = stack.pop()
            size += currPackage.getSizeBytes() 
            if size >= xyz:
                return True
            for dependency in currPackage.getDependencies():
                if dependency not in seen:
                    stack.append(dependency)
                    seen.add(dependency)
        return False 

        
    def packageDepends(self, package1, package2):
        pass


    def containsBlocklistLicense(self, blocklist):
        stack = [self.startingPackage]
        seen = set([self.startingPackage])
        while stack:
            currPackage = stack.pop()
            if currPackage.getLicense() in blocklist:
                return True
            for dependency in currPackage.getDependencies():
                if dependency not in seen:
                    stack.append(dependency)
                    seen.add(dependency)
        return False 
        



    











    
    
