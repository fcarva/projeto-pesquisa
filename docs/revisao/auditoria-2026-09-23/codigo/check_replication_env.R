.libPaths(c("C:/Users/DELL/Documents/projeto-pesquisa/projeto-pesquisa/renv/library/windows/R-4.6/x86_64-w64-mingw32", .libPaths()))
pkgs <- c("arrow", "data.table", "contdid", "ptetools", "npiv", "did", "HonestDiD", "synthdid")
for (p in pkgs) {
  cat(p, ": ")
  tryCatch({
    loadNamespace(p)
    d <- packageDescription(p)
    cat(as.character(d$Version), " sha=", ifelse(is.null(d$RemoteSha), "NA", d$RemoteSha), "\n", sep="")
  }, error=function(e) cat("ERROR", conditionMessage(e), "\n"))
}
print(sessionInfo())
